import numpy as np


def generate_digit(max_num_digits):
    return np.random.randint(1, np.power(10, max_num_digits))

'''
Input may optionally be reversed, shown to increase performance in many tasks in:
"Learning to Execute"
http://arxiv.org/abs/1410.4615
and
"Sequence to Sequence Learning with Neural Networks"
http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf
'''
def load_data(num_examples=50000, max_num_digits=3, reverse=False):
    # Maximum length of input is 'int + int' (e.g., '345+678'). Maximum length of
    # int is max_num_digits.
    maxlen = 2 * max_num_digits + 1

    questions = []
    expected = []
    seen = set()
    while len(questions) < num_examples:
        a = generate_digit(max_num_digits)
        b = generate_digit(max_num_digits)
        # Skip any addition questions we've already seen
        # Also skip any such that x+Y == Y+x (hence the sorting).
        key = tuple(sorted((a, b)))
        if key in seen:
            continue
        seen.add(key)
        query = '{}+{}'.format(a, b)
        ans = str(a + b)
        if reverse:
            # Reverse the query, e.g., '12+345  ' becomes '  543+21'. (Note the
            # space used for padding.)
            query = query[::-1]
        questions.append(query)
        expected.append(ans)
    return questions, expected
