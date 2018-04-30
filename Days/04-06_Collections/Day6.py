# Trying to use what I learned in this chapter
# Not totally working like I want yet

import collections
import csv

data_file = "Florida.csv"

Candidate_votes = collections.namedtuple("Candidate_votes", "county votes")

def get_votes_by_candidate(data=data_file):
    '''

    '''
    results = collections.defaultdict(list)
    with open(data) as f:
        reader = csv.reader(f)
        first_row = next(reader)
        for line in reader:
            if line == first_row:
                continue
            else:
                county = line[0]
                for k, v in enumerate(line):
                    if v == "" or v == "Total":
                        continue
                    else:
                        candidate = first_row[k]
                        votes = line[k]
                    m = Candidate_votes(county=county, votes=votes)
                    results[candidate].append(m)
            del results[""]
            del results["Total"]

    return results

result_data = get_votes_by_candidate()

print(result_data)
