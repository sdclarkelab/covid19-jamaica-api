import connexion
from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./')
app.add_api('covid19_jam_openapi.yaml', validate_responses=True, strict_validation=True,
            options={"swagger_ui": True})

# Add CORS support
CORS(app.app)

if __name__ == '__main__':
    app.run()
