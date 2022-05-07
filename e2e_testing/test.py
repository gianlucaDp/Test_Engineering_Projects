
def test_move_same_get_eaten(main_page):
    """
    Start a game, move the same piece twice and get eaten. Restart the game
    """
    main_page.restart_game()
    move_successful = main_page.move_player_piece("42", "53")
    assert move_successful
    main_page.wait_for_opponent()
    destination = "64"
    tile = main_page.get_tile(destination)
    # Opponent had only one move, if left position is not free right one is
    if not main_page.is_tile_free(tile):
        destination = "44"
    move_successful = main_page.move_player_piece("53", destination)
    assert move_successful
    main_page.wait_for_opponent()
    # The previous position will be empty if the player's piece have been eaten
    tile = main_page.get_tile(destination)
    assert main_page.is_tile_free(tile)
    main_page.restart_game()
