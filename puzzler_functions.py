""" CSC108: Fall 2020 -- Assignment 1: Phrase Puzzler Functions

UTM Instructors: Michael Liut, Larry Zhang, Andi Bergen

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all sub-directories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Diane Horton, 
Tom Fairgrieve, Michael Liut, Jacqueline Smith, and Anya Tafliovich.
"""

from constants import (CONSONANT_POINTS, VOWEL_PRICE, CONSONANT_BONUS,
                       PLAYER_ONE, PLAYER_TWO, VOWEL, ALL_CONSONANTS,
                       SOLVE, QUIT, HUMAN, HUMAN_HUMAN,
                       HUMAN_COMPUTER, EASY, HARD, CONSONANT,
                       ALL_VOWELS, PRIORITY_CONSONANTS, HIDDEN)


# This function has been given as an example. 
def is_win(puzzle: str, view: str) -> bool:
    """ Return True if and only if <puzzle> and <view> are a winning
        combination. That is, if and only if <puzzle> and <view> are the same.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    >>> is_win('apple', 'app')
    False
    
    """

    return puzzle == view


# This function has been given as an example of using a helper function.
def is_game_over(puzzle: str, view: str, move: str) -> bool:
    """ Return True if and only if <puzzle> and <view> are a 
        winning combination or <move> is QUIT.

    >>> is_game_over('apple', 'a^^le', 'V')
    False
    >>> is_game_over('apple', 'a^^le', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True

    """

    return move == QUIT or is_win(puzzle, view)


# This helper function finds if current player is human or not.
def is_human(current_player: str, game_type: str) -> bool:
    """ Return True if and only if <current_player> represents a human in a
        game of type <game_type>.

        <current_player> is PLAYER_ONE or PLAYER_TWO.
        <game_type> is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.

        In a HUMAN game or a HUMAN_HUMAN game, a player is always
        human. In a HUMAN_COMPUTER game, PLAYER_ONE is human and
        PLAYER_TWO is computer.

    >>> is_human('Player One', 'H-')
    True
    >>> is_human('Player One', 'HH')
    True
    >>> is_human('Player Two', 'HH')
    True
    >>> is_human('Player One', 'HC')
    True
    >>> is_human('Player Two', 'HC')
    False

    """

    if game_type == HUMAN:
        return True
    elif game_type == HUMAN_HUMAN:
        return True
    elif game_type == HUMAN_COMPUTER and current_player == PLAYER_ONE:
        return True
    else:
        return False


# This helper function has been given as an example. 
def half_revealed(view: str) -> bool:
    """ Return True if and only if at least half of the alphabetic
        characters in <view> are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False

    """

    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic += 1
    return num_alphabetic >= num_hidden


# This helper function returns the score of current user
def current_player_score(player_one_score: int, player_two_score: int, current_player: str) -> int:
    """ <current_player> can be PLAYER_ONE or PLAYER_TWO.
        If <current_player> is equal to PLAYER_ONE then
        return player_one_score, otherwise return player_two_score

        >>> current_player_score(2, 1, 'Player One')
        2
        >>> current_player_score(4, 3, 'Player Two')
        3

        """
    if current_player == PLAYER_ONE:
        return player_one_score
    else:
        return player_two_score


def update_char_view(puzzle: str, view: str, index: int, guess: str) -> str:
    """ <puzzle> is the solution.
        <View> is current view.
        <index> is the current index of the view.
        <guess> is the guess made by player.

        Check if the guess made by player is right. If yes then
        return the character otherwise return HIDDEN.

        >>> update_char_view('abce' , 'a^ce', 0, 'd')
        'a'
        >>> update_char_view('abce' , 'a^ce', 1, 'b')
        'b'
        >>> update_char_view('abce' , 'a^ce', 3, 'f')
        'e'
        >>> update_char_view('rat' , 'ra^', 2, 'd')
        '^'
        >>> update_char_view('face' , 'fac^', 3, 'e')
        'e'

        """
    if view[index] != HIDDEN:
        return view[index]
    elif puzzle[index] == guess:
        return guess
    else:
        return HIDDEN


def calculate_score(score: int, num_occurrences: int, move: str) -> int:
    """ <score> is the current player score.
        <num_occurrences> is the number of occurrences of guess in the solution.
        <move> is the type of move player selected to guess.

        If <move> is 'C' then score should be increased by <num_occurrences> times
        the CONSONANT_POINTS. If the <move> is 'V' then score needs to be subtracted
        by VOWEL_PRICE, regardless of the <num_occurrences>.
        Finally the new score should be returned

        >>> calculate_score(2, 2, 'C')
        4
        >>> calculate_score(1, 3, 'V')
        0
        >>> calculate_score(2, 4, 'V')
        1
        >>> calculate_score(1, 4, 'C')
        5

        """
    if move == CONSONANT:
        score += num_occurrences * CONSONANT_POINTS
    elif move == VOWEL:
        score -= VOWEL_PRICE
    else:
        pass
    return score


def erase(string: str, guessed_string_index: int) -> str:
    """ <string> is the string that has to be updated.
        <guessed_string_index> is the index of the character that
        has to be removed from the string. It should be in range of length
        of <string>

        >>> erase('bdfp', 2)
        'bdp'
        >>> erase('bdfp', 1)
        'bfp'
        >>> erase('bdfp', 3)
        'bdf'

    """
    if guessed_string_index != -1:
        return string.replace(string[guessed_string_index], '')
    else:
        return string


def next_player(current_player: str, num_occurrences: int, game_type: str) -> str:
    """ Returns next player based on <current_player>, <num_occurrences> and <game_type>
        If <game_type> is HUMAN then always return PLAYER_ONE.
        Otherwise if <num_occurrences> is less than 1, <current_player> turn ends and
        return other player.

        >>> next_player('Player One', 0, 'H-')
        'Player One'
        >>> next_player('Player One', 2, 'H-')
        'Player One'
        >>> next_player('Player One', 0, 'HH')
        'Player Two'
        >>> next_player('Player Two', 3, 'HH')
        'Player Two'
        >>> next_player('Player One', 1, 'HC')
        'Player One'
        >>> next_player('Player Two', 0, 'HC')
        'Player One'

        """
    if game_type == HUMAN:
        return current_player
    else:
        if num_occurrences > 0:
            return current_player
        else:
            if current_player == PLAYER_ONE:
                return PLAYER_TWO
            else:
                return PLAYER_ONE


def is_one_player_game(game_type: str) -> bool:
    """ return True if and only if <game_type> is HUMAN,
        otherwise return False

        >>> is_one_player_game('H-')
        True
        >>> is_one_player_game('HH')
        False
        >>> is_one_player_game('HC')
        False

        """

    if game_type == HUMAN:
        return True
    else:
        return False


def computer_chooses_solve(view: str, difficulty: str, consonants: str) -> bool:
    """ returns true if and only if <game_type> is HARD and <view> has more than half characters revealed, that is,
        not HIDDEN.

        >>> computer_chooses_solve('^x^^', 'E', 'adf')
        False
        >>> computer_chooses_solve('^xe^', 'E', 'adf')
        False
        >>> computer_chooses_solve('^xe^', 'H', 'adf')
        False
        >>> computer_chooses_solve('axe^', 'H', 'df')
        True
        >>> computer_chooses_solve('^xed', 'H', 'af')
        True
    """
    if difficulty == EASY:
        return False
    else:
        if view.count(HIDDEN) < (len(view) / 2):
            return True
        else:
            return False


def is_hidden(index: int, puzzle: str, view: str) -> bool:
    """ returns true if and only if <index> position of <view> is equal
        to '^'

        >>> is_hidden(0, 'tree', '^^^^')
        True
        >>> is_hidden(1, 'tree', '^r^^')
        False
        >>> is_hidden(1, 'tree', '^^ee')
        True

        """
    return view[index] == HIDDEN


def is_bonus_letter(letter: str, puzzle: str, view: str) -> bool:
    """ returns False if and only if <letter> exists in <puzzle> and
        <letter> does not exists in <view> and <letter> does not exists is ALL_VOWELS

        >>> is_bonus_letter('b', 'branch', '^ranch')
        True
        >>> is_bonus_letter('a', 'branch', '^ranch')
        False
        >>> is_bonus_letter('b', 'tree', '^^^^')
        False
        >>> is_bonus_letter('b', 'umbrella', 'u^^^^lla')
        True

        """

    return puzzle.find(letter) != -1 \
           and view.find(letter) == -1 \
           and ALL_VOWELS.find(letter) == -1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
