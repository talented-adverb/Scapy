#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<arpa/inet.h>

//#include"myheader.h"

#define SRC_IP "1.2.3.4"
#define DEST_IP "10.0.2.15"
#define DST_PORT 9090

void send_raw_ip_packet(struct ipheader* ip);

void main(){
char buffer[PACKET_LEN];
memset(buffer,0,PACKET_LEN);

struct ipheader *ip=(struct ipheader *)buffer;
struct udpheader *udp=(struct udpheader *)(buffer + sizeof(struct ipheader));
char *data=buffer + sizeof(struct ipheader)+sizeof(udpheader);

}
