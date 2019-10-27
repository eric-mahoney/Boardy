from django.shortcuts import render
from .models import Board, Message, User

# Create your views here.
def get_homepage(request):
    return render(request, 'index.html')

def get_creator(request, username):
    creator = User.objects.get(username=username)
    boards = Board.objects.filter(creator=creator)
    messages = Message.objects.filter(creator=creator)
    return render(request, 'creator.html',
        {
            'creator': creator,
            'messages': messages,
            'boards': boards
        }
    )

def get_board(request, board_id):
    board = Board.objects.get(id=board_id)
    messages = Message.objects.filter(board=board)
    return render(request, 'board.html', {'board': board, 'messages': messages})

def get_message(request, message_id):
    message = Message.objects.get(id=message_id)
    return render(request, 'message.html', {'message': message})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def view_boards(request):
    boards = Board.objects.all()
    return render(request, 'boards.html', {'boards': boards})