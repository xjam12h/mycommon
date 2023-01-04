

def calc_MRR(rank_list):
    sum_value = sum([1/rank if rank!=0 else 0 for rank in rank_list])
    ans = sum_value / len(rank_list)
    return ans