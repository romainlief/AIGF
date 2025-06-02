#!/bin/zsh

SESSION_NAME=AIGirlFriend
tmux has-session -t $SESSION_NAME 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Session $SESSION_NAME déjà en cours. Fermeture..."
    tmux kill-session -t $SESSION_NAME
fi

tmux new-session -d -s $SESSION_NAME # Nouvelle session détachée
# Volet 1 : lancer ollama serve
tmux send-keys -t $SESSION_NAME 'echo Lancement de ollama... && ollama serve' C-m
sleep 1
tmux split-window -v -t $SESSION_NAME # Deuxième volet verticalement
# Volet 2 : activer l'environnement virtuel et lancer le script Python
tmux send-keys -t $SESSION_NAME 'cd ~/PythonProjects/AIGF && source chatbot/bin/activate && echo Environnement activé. Lancement de main.py... && python3 main.py' C-m
# Attache la session seulement après avoir tout configuré
tmux attach -t $SESSION_NAME