######################################################################################
### API Rest Residencias ## LABORATORIO PARA EL DESPLIEGUE DE APLICACIONES "AD-24" ###
######################################################################################

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)