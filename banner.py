def banner_text(text: str =" ", screen_width: int =80) -> None :
    """

    :param text:
    :param screen_width:
    :return: there is an exception that it returns "ValueError" if the input is longer than screen width.
    """
                                        #this adding of default value helps when no width is specified.
                                        #the default value 80 is used.
                                        # similarly for "text"
    # ** HANDLING INVALID INPUT
    # -> SEE THE TYPES OF ERROR THAT CAN BE RAISED IN PYTHON DOCUMENTATION
    if len(text)> screen_width-4:
        raise ValueError("String '{}' is larger than the specified width {}."
                         .format(text, screen_width))

    if text == '*':
        print("*"*screen_width)

    else:
        print("**{}**".format(text.center(screen_width-4)))


banner_text('*')
banner_text('Always look on the bright side of the life.')
banner_text('If life seems jolly rotten',54)    #here we specify the screenwidth
banner_text('There\'s something you have forgotten')    #here we DON'T specify the screenwidth
banner_text('And that\'s to laugh and smile and dance and sing',92)  #here we specify the screenwidth
banner_text('*')
