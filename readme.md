# Flask Skeleton App 创建流程
1. create factory app in app/init.py, alternatively, create instance in app/init.py but not app-factory
2. create app instance Config class
3. create initialize of plugins
   - SqlAlchemy init
   - migrate init, **CAUTION!** PLEASE IMPORT MODELS WHEN MIGRATE INIT_APP(), OTHERWISE MODEL WOULDN'T BE DETECTED
    ```python
      from flask_migrate import Migrate
      from admin.extensions.init_sqlalchemy import db
      from admin.models import Dept
         
      migrate = Migrate()
         
         
      def init_migrate(app):
          migrate.init_app(app, db)
      ```
4. create blueprint initialize


# Flask admin extends Flask Skeleton App 创建流程
there is something keep in mind when you coding
```text
`/admin` build by flask-admin, when you initialize flask app instance
```

## 创建script : admin_init_command
```python
from flask import Flask
from flask.cli import AppGroup

# app/common/script/init
def init_scripts(app: Flask):
    app.cli.add_command(admin_cli)

    
# app/common/script/admin
admin_cli = AppGroup('admin')
@admin_cli.command('init')
def init_admin():
     db.session.add(post)
     # ...
     db.session.commit()
     
     print('inject user')

```


## create views
详见 flask-admin官方示例：https://github.com/flask-admin/flask-admin/tree/master/examples/sqla