#!/bin/bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=entropy-dummy" >/dev/null 2>&1

echo "const uint8_t a_private_key[] = {" > entropy-zero-fw/main/private_key.h
xxd -i key.pem | sed -e 's/unsigned char key_pem\[\] = {//' -e 's/unsigned int key_pem_len.*//' -e 's/};//' >> entropy-zero-fw/main/private_key.h
echo ",0x00};" >> entropy-zero-fw/main/private_key.h

echo "const uint8_t a_cert_pem[] = {" > entropy-zero-fw/main/cert_pem.h
xxd -i cert.pem | sed -e 's/unsigned char cert_pem\[\] = {//' -e 's/unsigned int cert_pem_len.*//' -e 's/};//' >> entropy-zero-fw/main/cert_pem.h
echo ",0x00};" >> entropy-zero-fw/main/cert_pem.h

echo "const uint8_t certs_root_CA_crt[] = {0x00};" > entropy-zero-fw/main/root_crt.h

rm key.pem cert.pem
