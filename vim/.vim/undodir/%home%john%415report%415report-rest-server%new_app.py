Vim�UnDo� Y�����2����֎5Fb�\>q@dS����v                     '       '   '   '    Y��6    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                       �                  �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                 app = Flask(__name__)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                 app = Flask(__name__)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                     app = Flask(__name__)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �               def create_app():5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                  5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             Y���    �                     db.init_app(app)5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             Y��U     �                   db.init_app(app)5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             Y��j     �                   app = Flask(__name__)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y��~     �                 5�_�                       6    ����                                                                                                                                                                                                                                                                                                                                                             Y���    �               D    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'5�_�                           ����                                                                                                                                                                                                                                                                                                                                         $       v   $    Y��     �                $from flask import Flask, current_app   from models_sqla import db5�_�                           ����                                                                                                                                                                                                                                                                                                                                         $       v   $    Y��     �                1from flask import Flaskfrom models_sqla import db5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                         $       v   $    Y��"     �               C    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                         $       v   $    Y��"     �               B    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mp/test.db'5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                         $       v   $    Y��"     �               A    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///p/test.db'5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                         $       v   $    Y��#    �               @    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���     �               def create_app():5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���     �               def create_app(Config):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���     �         	      def create_app(Config):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���     �         	      def create_app(config):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���     �         	      ?    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'5�_�                       @    ����                                                                                                                                                                                                                                                                                                                                                             Y���     �      	   	      @    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                if __name__ == '__main__':�   	                  return app5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                 &    app = create_app(DevelopmentConfi)5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                 '    app = create_app(DevelopmentConfig)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��5     �                     app.runt()5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             Y��c    �                @    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                5�_�       "           !      )    ����                                                                                                                                                                                                                                                                                                                                                             Y���     �      	         )    app.config.from_object(configuration)5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                             Y��     �      	         +    #Initialize database and create tables.5�_�   "   $           #   	       ����                                                                                                                                                                                                                                                                                                                                                             Y��     �                   db.init_app(app)5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                                                             Y��#    �               def create_app(configuration):5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                                                             Y��     �                5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             Y��%     �                   app.register_blueprint(api)5�_�   &               '           ����                                                                                                                                                                                                                                                                                                                                                             Y��5    �               def create_app(configuration):5��