# SUBDB_DATABASE_TABLES = {
#     'persons' : 'subdb',
# }

# class Router(object):
#     def db_for_read(self, model, **hints):
#         if model._meta.db_table in SUBDB_DATABASE_TABLES:
#             return SUBDB_DATABASE_TABLES[model._meta.db_table]
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.db_table in SUBDB_DATABASE_TABLES:
#             return SUBDB_DATABASE_TABLES[model._meta.db_table]
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         return True

#     def allow_migrate(self, db, app_label, model=None, **hints):
#         if db == "subdb":
#             if model is not None and model._meta.db_table in SUBDB_DATABASE_TABLES:
#                 return True
#             return False
#         else:
#             if model is not None and model._meta.db_table in SUBDB_DATABASE_TABLES:
#                 return False
#             return True