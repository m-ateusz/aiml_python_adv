from enum import Flag, IntEnum, StrEnum, Enum, auto, verify, UNIQUE, NAMED_FLAGS, CONTINUOUS


class Perm(StrEnum):
   SUID = 'suid'
   READ = 'read'
   WRITE = 'write'
   EXECUTE = 'execute'

for item in Perm:
   print(item.value, item.name)


perm = Perm('execute')

if perm == Perm.READ: pass
if perm == Perm.WRITE: pass
if perm == Perm.EXECUTE: pass
