#autokey script - utf characters workaround for polish language  by grizz - Witek Firlej http://grizz.pl
# ver. 2015.03.06.1
# Copyright (C) 2015 Witold Firlej

retCode, input_text = dialog.input_dialog("Autokey utf workaound PL", "Podaj tekst")

output_text = input_text.decode("utf-8")

mapping = [ (u'ą', '<alt_gr>+a'), \
            (u'ć', '<alt_gr>+c'), \
            (u'ę', '<alt_gr>+e'), \
            (u'ł', '<alt_gr>+l'), \
            (u'ń', '<alt_gr>+n'), \
            (u'ó', '<alt_gr>+o'), \
            (u'ś', '<alt_gr>+s'), \
            (u'ź', '<alt_gr>+x'), \
            (u'ż', '<alt_gr>+z'), \
            (u'Ą', '<alt_gr>+<shift>+a'), \
            (u'Ć', '<alt_gr>+<shift>+c'), \
            (u'Ę', '<alt_gr>+<shift>+e'), \
            (u'Ł', '<alt_gr>+<shift>+l'), \
            (u'Ń', '<alt_gr>+<shift>+n'), \
            (u'Ó', '<alt_gr>+<shift>+o'), \
            (u'Ś', '<alt_gr>+<shift>+s'), \
            (u'Ź', '<alt_gr>+<shift>+x'), \
            (u'Ż', '<alt_gr>+<shift>+z') ]

for k, v in mapping:
    output_text = output_text.replace(k, v)

clipboard.fill_clipboard(output_text)



