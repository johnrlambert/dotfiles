Vim�UnDo� �ŭ��
����X_��.�n�]��9�                                      ]1α    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]1�M    �      
         def create_app(configuration):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]1Ξ    �                import sqltap.wsgi5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]1Ϋ     �                2from nplusone.ext.flask_sqlalchemy import NPlusOne5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]1ί     �                =    app.wsgi_app = sqltap.wsgi.SQLTapMiddleware(app.wsgi_app)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]1ΰ    �                    NPlusOne(app)5��