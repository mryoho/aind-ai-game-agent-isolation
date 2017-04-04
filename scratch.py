num_moves = list()
    next_moves = list()
    index = 0
    max_move_index = 0
    max_num_moves = 0
    best_move = (int,int)
    print(game.to_string())
    print(game.get_legal_moves())
    #print(game.active_player)
    for move in game.get_legal_moves():
        logging.debug('Move: ' + str(move))
        next_move = game.forecast_move(move)
        print(next_move.to_string())
        next_moves.append(next_move)
        print(next_move.get_legal_moves(player=next_move.inactive_player))
        num_move = len(next_move.get_legal_moves(player=next_move.inactive_player))
        logging.debug('Num Moves: ' + str(num_move))
        num_moves.append(num_move)
        if num_move > max_num_moves:
            best_move = move
            max_move_index = index
        index += 1

    return float(max_num_moves), move

    def min_value_minimax(game, depth):
          """Implement the minimax search algorithm as described in the lectures.

          Parameters
          ----------
          game : isolation.Board
              An instance of the Isolation game `Board` class representing the
              current game state

          depth : int
              Depth is an integer representing the maximum number of plies to
              search in the game tree before aborting
          """
          if len(game.get_legal_moves()) == 0:
              return game.utility()

          v = float("inf")
          for move in game.get_legal_moves():
              v = min(v, max_value_minimax(game.forecast_move(move), depth + 1))

          return v

      def max_value_minimax(game, depth):
          """Implement the minimax search algorithm as described in the lectures.

          Parameters
          ----------
          game : isolation.Board
              An instance of the Isolation game `Board` class representing the
              current game state

          depth : int
              Depth is an integer representing the maximum number of plies to
              search in the game tree before aborting
          """
          if len(game.get_legal_moves()) == 0:
              return game.utility()

          v = float("-inf")
          for move in game.get_legal_moves():
              v = max(v, min_value_minimax(game.forecast_move(move), depth + 1))

          return v
