@echo off
start python backend/profile.py
start python backend/image.py
start python backend/recommendation.py
start python backend/match_receiver.py
start python backend/match.py

start python backend/chatms/chat.py
start python backend/chatms/chatsocketone.py
start python backend/chatms/chatsockettwo.py
start python backend/chatms/chatsocketthree.py
start python backend/chatms/chatsocketfour.py
start python backend/chatms/chatsocketfive.py

start docker pull alwynong/account:1.0.0 & docker run -p 8000:8000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/sglovelah_account alwynong/account:1.0.0