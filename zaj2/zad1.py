from sqlalchemy import *
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

inspector = inspect(engine)
table_names = inspector.get_table_names()
#print(table_names)

metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)
state_fact = Table('state_fact', metadata, autoload_with=engine)
#print(repr(census))


# Nazwy stanów występujące w bazie
stmt = text('SELECT name FROM state_fact')
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results)

# Policz populacje w stanie Alaska oraz New York w 2000 oraz 2008 roku
stmt = select(
func.sum(census.c.pop2000), func.sum(census.c.pop2008)
).where(census.c.state == 'Alaska' or census.c.state == 'Illinois')
results = connection.execute(stmt).fetchall()
sum_pop2000, sum_pop2008 = results[0]
sum_pop = sum_pop2008 + sum_pop2008
print(sum_pop)

# Policz liczbę kobiet oraz mężczyzn w stanie New York w 2008 roku
stmt = select(
func.sum(census.c.pop2008)
).where(census.c.state == 'New York' and census.c.sex == 'F')
results = connection.execute(stmt).fetchall()
women_count = results[0][0]
stmt = select(
func.sum(census.c.pop2008)
).where(census.c.state == 'New York' and census.c.sex == 'M')
results = connection.execute(stmt).fetchall()
men_count = results[0][0]
print(f"F: {women_count}, M:{men_count}")


