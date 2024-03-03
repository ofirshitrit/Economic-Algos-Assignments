from abcvoting.preferences import Profile
from abcvoting import abcrules
from abcvoting import misc

profile = Profile(num_cand=8)

v1 = [0, 3, 4, 7]
v2 = [1, 2, 5]
v3 = [0, 3]
v4 = [1, 4, 5]
v5 = [0, 2, 6]
v6 = [3, 6, 7]

voters = [misc.CandidateSet(v) for v in [v1, v2, v3, v4, v5, v6]]

profile.add_voters(voters)

rule_id = "equal-shares-with-increment-completion"
# rule_id = "equal-shares"
committee_size = 5

result5 = abcrules.compute(rule_id, profile, committeesize=committee_size)
winning_committee5 = set(result5[0])
print(f"The committee size is {committee_size}: {winning_committee5}")

committee_size = committee_size + 1
result6 = abcrules.compute(rule_id, profile, committeesize=committee_size)
winning_committee6 = set(result6[0])
print(f"The committee size is {committee_size}: {winning_committee6}")

