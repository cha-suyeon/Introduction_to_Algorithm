# Better way

# 파이썬의 버전 확인
# 파이썬 내장 모듈 `sys` 의 값을 검사해서 버전을 알 수 있음

import sys
print(sys.version_info)
print(sys.version)

# 출력값
# sys.version_info(major=3, minor=10, micro=8, releaselevel='final', serial=0)
# 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]