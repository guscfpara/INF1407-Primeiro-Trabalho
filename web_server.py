import mimetypes
import platform

from time import gmtime, strftime

def client_request(connection, client, config):
    # Receive message received from socket
    message = connection.recv(client[1])
    message = message.decode(config['code'])
    
    if not message:
        # No message received from socket, closing request
        connection.close()
        return

    # Request receives the first line of the request
    request = message.splitlines()[0]

    # Separate method, file path and HTTP protocol
    method, archive_path, protocol = request.split(' ')

    if (method != 'GET'):
        # If the method is not GET, warn the user that the method is not supported by the server
        body=b'METHOD NOT SUPORTED'
        status_code='501'
        status_text='METHOD {0} NOT SUPORTED'.format(method)
        content_type = ''

    else:
        print(f'Tentando abrir {archive_path}...\n')
        try:
            # If it receives a file request and finds it, send selected file
            with open(archive_path[1:],'rb') as f:
                body=f.read()
            content_type = mimetypes.guess_type(archive_path[1:])[0]
            status_code='200'
            status_text='OK'

        except FileNotFoundError:
            # If the file is not found, look in the list of default files or send to 404
            flag = False
            # Compare the files that are in the list
            for file in config['defaults_files']:
                archive_path = archive_path.split('/')[-1]
                if archive_path in file and archive_path != '':
                    file = '{0}/{1}'.format(config['local_dir'],file)
                    flag = True
                    break
            # If you find it on the list, send it to 200
            if flag:
                status_code='200'
                status_text='OK'
            # If not, send 404
            else:
                file = '{0}/{1}'.format(config['local_dir'],config['error_file'])
                status_code='404'
                status_text='FILE NOT FOUND'
            # Open the file and send in the body
            with open(file,'rb') as f:
                    body=f.read()
            # Get the file type
            content_type = mimetypes.guess_type(file)[0]            

        except OSError:
            # Warn operating system error
            file = '{0}/{1}'.format(config['local_dir'],config['error_file'])
            # Open the file and send in the body
            with open(file,'rb') as f:
                    body=f.read() 
            status_code='500'
            status_text='FAILED OPENING FILE'
            content_type = mimetypes.guess_type(file)[0]  

        except UnicodeDecodeError:
            # Warn decoding error
            file = '{0}/{1}'.format(config['local_dir'],config['error_file'])
            # Open the file and send in the body
            with open(file,'rb') as f:
                    body=f.read() 
            status_code='500'
            status_text='FAILED OPENING FILE'
            content_type = mimetypes.guess_type(file)[0]  

    # Format Response Header
    response_header = [
        f'{protocol} {status_code} {status_text}',
        f'Server: {platform.platform()} ',
        f'Content-Type: {content_type}',
        f'Content-Length: {len(body)}',
        f'Date : {strftime("%a, %d %b %Y %I:%M:%S %p %Z", gmtime())}',
        f'Connection: close',
    ]

    # Format Response
    connection.send(''.join(response_header).encode(config['code']))
    connection.send('\n\n'.encode(config['code']))
    connection.send(body)

    # View Full Request and Response
    print(message)
    for el in response_header : print(el)
    print('Body : ', body)

    connection.close()