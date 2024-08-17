import sqlite3


class SQLighter:
    def __init__(self, database_file):
        """Подключение к БД и сохранение курсора соединения"""
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

# Есть ли пользователь в таблице
    def get_account(self, value, method):
        if method == 'name':     #(по имяни)
            with self.connection:
                result = self.cursor.execute('SELECT * FROM `account_date` WHERE `user_name` = ?',
                                             (value,)).fetchall()
                return bool(len(result))
        if method == 'number':     #(по номеру)
            with self.connection:
                result = self.cursor.execute('SELECT * FROM `account_date` WHERE `number` = ?',
                                             (value,)).fetchall()
                return bool(len(result))
        