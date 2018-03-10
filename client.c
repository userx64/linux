//linux TCP client e DNS lookup
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

#define MESSAGE "Test socket"

void err(char *msg){
    printf("Errore in %s\n", msg);
    exit(-1);
}
void uso(char argv[]){
    printf("Uso: %s <host> <porta>\n", argv);
    printf("Uso: %s --lookup <host>\n", argv);
    exit(0);
}

int main(int argc, char *argv[]){
    if(argc != 3)
	uso(argv[0]);

    if(strcmp(argv[1], "--lookup") == 0){
        struct hostent *hostinfo;
	struct in_addr *address;

	char host[32];

	strcpy(host, argv[2]);

	hostinfo = gethostbyname(host);

	if(hostinfo != NULL){
	    address = (struct in_addr *)hostinfo->h_addr;
	    printf("L'indirizzo per %s e' %s\n", host, inet_ntoa(*address));
	    return 1;
	}
	printf("Nessun indirizzo per %s\n", host);
	return 2;
    } 

    int sock, porta = atoi(argv[2]);
    struct sockaddr_in server;
    u_char host[64];
    strcpy(host, argv[1]);

    if((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1)
	err("in socket()");

    server.sin_family = AF_INET;
    server.sin_port = htons(porta);
    server.sin_addr.s_addr = inet_addr(host);
    memset(&(server.sin_zero), '\0', 8);
    if(connect(sock, (struct sockaddr *) &server, sizeof(server)) == -1)
	err("in connect()");

    printf("Connesso a %s:%d\n", host, porta);

    if(send(sock, MESSAGE, strlen(MESSAGE), 0) == -1)
	err("in send()");

    printf("'%s' inviato...\n", MESSAGE);

    close(sock);
    return 3;

}
