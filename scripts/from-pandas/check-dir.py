dir_before_import = set(dir())

from pandas import *

dir_after_import = set(dir()) - dir_before_import - {"vars_before_import"}
print(*sorted(dir_after_import, key=str.casefold), sep="\n")
