"""
This is a game to warm up the fingers for typing.


"""
import curses

def load_word_file(fileName):

    words = []
    with open(fileName, 'r') as f:
        for line in f:
            words += line.split(' ')
            words = [ w.replace('\n', '') for w in words]
    return words

if __name__ == '__main__':

    # curses stuff
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)


    # Draw start
    stdscr.addstr(0, 10, "Warm-Up Typing game")
    stdscr.refresh()

    # init
    words = load_word_file('text.txt')
    written_words = ['']
    cur_str = 0
    ww_x = 5
    ww_max_len = 40

    for i in range(len(words)):

        # type out the word
        word = words[i]
        new_word = ''
        preview_words = []
        clear_word = ' '*60
        new_word_axis = ww_x + 7
        word_to_write_axis = ww_x + 5

        for j in range(5, -4, -1):
            if j == 0:
                preview_words.append('[{}]'.format(word))
            elif i - j >= 0 and i - j < len(words):
                preview_words.append(words[i-j])

        stdscr.addstr(word_to_write_axis, 1, clear_word)
        stdscr.addstr(word_to_write_axis, 1, ' '.join(preview_words))

        # clear old word and move cursor
        stdscr.addstr(new_word_axis, 1, clear_word)
        stdscr.addstr(new_word_axis, 1, '')

        # update
        stdscr.refresh()

        while new_word != (word+' '):
            key = stdscr.getch()
            if key == 127:

                new_word = new_word[:-1]
                stdscr.addstr(new_word_axis, 1, clear_word)
                stdscr.addstr(new_word_axis, 1, new_word)
            else:

                new_word += str(chr(key))
                stdscr.addstr(new_word_axis, 1, new_word)

            # update keyboard input
            stdscr.refresh()

        if len(written_words[cur_str]) > ww_max_len:
            cur_str += 1
            written_words.append(word)
        else:
            written_words[cur_str] += ' ' +  word

    # end game
    curses.endwin()
