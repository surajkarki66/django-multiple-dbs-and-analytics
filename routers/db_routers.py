class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {"auth", "contenttypes", "admin", "sessions"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes, models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth_db"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes, models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "auth_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "auth_db"
        return None


class College:
    route_app_labels = {"college"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "college_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "college_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "college_db"
        return None


class University:
    route_app_labels = {"university"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "university_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "university_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "university_db"
        return None


class Organization:
    route_app_labels = {"organization"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "organization_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "organization_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "organization_db"
        return None

class Book:
    route_app_labels = {"book"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "book_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "book_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "book_db"
        return None
