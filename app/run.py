from flask import Flask
## aplicando autenticacion
from flask_jwt_extended import JWTManager
from app.controllers.dulce_controller import dulce_bp
## aplicando autenticacion
from app.controllers.user_controller import user_bp
from flask_swagger_ui import get_swaggerui_blueprint
from app.database import db

app = Flask(__name__)
## Configuracion de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "bucle"

# Configura la URL de la documentacion OpenAPI
SWAGGER_URL = "/api/docs" # Ruta para servir Swagger UI
API_URL = "/static/swagger.json"  # Ruta de tu archivo OpenAPI/Swagger
# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Dulceria API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configuracion de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dulceria.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Inicializa la base de datos
db.init_app(app)

## Inicializa la extension JWTManager
jwt = JWTManager(app)
# Registra el blueprint de animales en la aplicacion
app.register_blueprint(dulce_bp, url_prefix='/api')
## regitras el bleprint de users en la aplicacion
app.register_blueprint(user_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()
# Ejecuta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)