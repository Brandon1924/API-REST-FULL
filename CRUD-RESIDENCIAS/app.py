######################################################################################
### API Rest Residencias ## LABORATORIO PARA EL DESPLIEGUE DE APLICACIONES "AD-24" ###
######################################################################################
### * Monjaraz Perez Sara Alexandra   * Usuario GitHub SaraAlexMP                  ###
### * García Solís Francisco          * Usuario GitHub Upstagebunion               ###
### * Brandon                         * Usuario GitHub Brandon1924                 ###
### * Miguel Angel Loza Lopez         * Usuario GitHub Esblad                      ###
######################################################################################

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)