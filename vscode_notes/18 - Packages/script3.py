# packages shouldn't use deeply nested directory structures. except for absolutely huge collection of 
# code, there should be no need for them. for most pacages, a single top level directory is all thats needed


# altrough you can use the __all__ attrivute to hide names from 'from ... import *' by not listing
# those names, doing so propably is not a good idea, because its inconsistent