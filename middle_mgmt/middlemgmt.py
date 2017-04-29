def count_upper(word):
    return sum(1 for ch in word if ch.isupper())

ok = []

with open('2600_phrases_for_effective_performance_reviews.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            words = line.split()
            if len(words) == 1:
                continue
            if 'and' in words:
                words.remove('and')
            nonupper_words = [word for word in words if not word[0].isupper()]

            if len(nonupper_words) > 0:
                ok.append(line)
            else:
                continue
                print(line)

with open('phrases.txt', 'w') as f:
    f.write('\n'.join(ok))

            # if there are more than one uppercase letter,
            # it may be a heading
            # n_upper = sum(1 for ch in line if ch.isupper())
            # if n_upper > 1:
                # adj_upper = 0
                # for ch in line:
                    # adj_upper = adj_upper + 1 if ch.isupper() else 0
                    # if adj_upper > 1:
                        # break
                # if adj_upper > 1:
                    # continue
                # else:
                    # print(line)