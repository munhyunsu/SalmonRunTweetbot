import random


class RandomSelector(object):
    def __init__(self, *args):
        if len(args) < 1:
            raise EnvironmentError
        self.tables = args

    def get_random(self, ctx, args=()):
        base_table = self.tables[0]
        selected_item = random.choice(base_table)
        result_string = '{0.author.mention} {1}'.format(ctx,
                                                        selected_item)
        for locale_table in self.tables[1:]:
            result_string = '{0}/{1}'.format(result_string,
                                             locale_table[selected_item])
        return result_string
