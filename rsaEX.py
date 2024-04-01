import rsa

#Bob generates his public/private key pair and shares the public key with Alice
(bob_pub, bob_priv) = rsa.newkeys(2048) 
print("Bob Public: ", bob_pub, "\n") 
print("Bob Private: ", bob_priv, "\n") 

#Alice generates her public/private key pair and shares the public key with Bob 
(alice_pub, alice_priv) = rsa.newkeys(2048) 
print("Alice Public: ", alice_pub, "\n") 
print("Alice Private: ", alice_priv, "\n")

#Alice writes a message and encrypts it with Bob's public key
message = 'jctf{HAHAHA I knew you would intercept this transmission. You may have won this round, but there are many more challenges for me to best you at}'.encode('utf8') 
ciphertext = rsa.encrypt(message, bob_pub)
print("Ciphertext encrypted with Bob public: ", ciphertext, "\n")

#Bob receives the message, and decrypts it with his private key 
decryptedMessage = rsa.decrypt(ciphertext, bob_priv) 
print(decryptedMessage.decode('utf8'))


