from macko.controller import simple_controller


def register_blueprint_handle(app):
    controllers = [
        simple_controller
    ]
    for controller in controllers:
        app.register_blueprint(controller.blueprint)
