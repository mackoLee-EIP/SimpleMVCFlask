from macko.utils.my_exceptions import BadRequest, InternalServerError, Unauthorized


def error_handle(app):
    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        return {
            'description':'Parameter가 잘못됨 (범위, 값 등)',
            'code':400
        }, 400
    app.register_error_handler(400, handle_bad_request)

    @app.errorhandler(Unauthorized)
    def handle_unauthorized(e):
        return {
            'description':'인증을 위한 Header가 잘못됨',
            'code':401
        }, 401
    app.register_error_handler(401, handle_unauthorized)

    @app.errorhandler(InternalServerError)
    def handle_internal_server_error(e):
        return {
            'description':'서버 에러, 채팅으로 문의 요망',
            'code':500
        }, 500
    app.register_error_handler(500, handle_internal_server_error)
