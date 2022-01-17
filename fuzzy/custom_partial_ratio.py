import Levenshtein
from Levenshtein.StringMatcher import StringMatcher

CPU_ERROR_PATTERN = "[Hardware Error]: CPU:"
line = r'[ 9080.511319] [Hardware Error]: CPU:143 (19:1:1) MC2_STATUS[-|CE|MiscV|AddrV|-|-|SyndV|CECC|-|-|-]: 0x9c30400004020166'


Higher_matcher_tuple = max(StringMatcher(CPU_ERROR_PATTERN, line).get_matching_blocks(), key=lambda x: x[2])
line_start = Higher_matcher_tuple[1] - Higher_matcher_tuple[0]
line_end = line_start + Higher_matcher_tuple[-1]
match = StringMatcher(None, CPU_ERROR_PATTERN, line[line_start:line_end])
match.ratio()