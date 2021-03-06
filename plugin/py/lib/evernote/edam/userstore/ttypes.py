#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *
import evernote.edam.type.ttypes
import evernote.edam.error.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class PublicUserInfo(object):
  """
   This structure is used to provide publicly-available user information
   about a particular account.
  <dl>
   <dt>userId:</dt>
     <dd>
     The unique numeric user identifier for the user account.
     </dd>
   <dt>shardId:</dt>
     <dd>
     The name of the virtual server that manages the state of
     this user. This value is used internally to determine which system should
     service requests about this user's data.  It is also used to construct
     the appropriate URL to make requests from the NoteStore.
     </dd>
   <dt>privilege:</dt>
     <dd>
     The privilege level of the account, to determine whether
     this is a Premium or Free account.
     </dd>
   </dl>
  
  Attributes:
   - userId
   - shardId
   - privilege
   - username
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'userId', None, None, ), # 1
    (2, TType.STRING, 'shardId', None, None, ), # 2
    (3, TType.I32, 'privilege', None, None, ), # 3
    (4, TType.STRING, 'username', None, None, ), # 4
  )

  def __init__(self, userId=None, shardId=None, privilege=None, username=None,):
    self.userId = userId
    self.shardId = shardId
    self.privilege = privilege
    self.username = username

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.userId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.shardId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.privilege = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.username = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PublicUserInfo')
    if self.userId != None:
      oprot.writeFieldBegin('userId', TType.I32, 1)
      oprot.writeI32(self.userId)
      oprot.writeFieldEnd()
    if self.shardId != None:
      oprot.writeFieldBegin('shardId', TType.STRING, 2)
      oprot.writeString(self.shardId)
      oprot.writeFieldEnd()
    if self.privilege != None:
      oprot.writeFieldBegin('privilege', TType.I32, 3)
      oprot.writeI32(self.privilege)
      oprot.writeFieldEnd()
    if self.username != None:
      oprot.writeFieldBegin('username', TType.STRING, 4)
      oprot.writeString(self.username)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthenticationResult(object):
  """
   When an authentication (or re-authentication) is performed, this structure
   provides the result to the client.
  <dl>
   <dt>currentTime:</dt>
     <dd>
     The server-side date and time when this result was
     generated.
     </dd>
   <dt>authenticationToken:</dt>
     <dd>
     Holds an opaque, ASCII-encoded token that can be
     used by the client to perform actions on a NoteStore.
     </dd>
   <dt>expiration:</dt>
     <dd>
     Holds the server-side date and time when the
     authentication token will expire.
     This time can be compared to "currentTime" to produce an expiration
     time that can be reconciled with the client's local clock.
     </dd>
   <dt>user:</dt>
     <dd>
     Holds the information about the account which was
     authenticated if this was a full authentication.  May be absent if this
     particular authentication did not require user information.
     </dd>
   <dt>publicUserInfo:</dt>
     <dd>
     If this authentication result was achieved without full permissions to
     access the full User structure, this field may be set to give back
     a more limited public set of data.
     </dd>
   </dl>
  
  Attributes:
   - currentTime
   - authenticationToken
   - expiration
   - user
   - publicUserInfo
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'currentTime', None, None, ), # 1
    (2, TType.STRING, 'authenticationToken', None, None, ), # 2
    (3, TType.I64, 'expiration', None, None, ), # 3
    (4, TType.STRUCT, 'user', (evernote.edam.type.ttypes.User, evernote.edam.type.ttypes.User.thrift_spec), None, ), # 4
    (5, TType.STRUCT, 'publicUserInfo', (PublicUserInfo, PublicUserInfo.thrift_spec), None, ), # 5
  )

  def __init__(self, currentTime=None, authenticationToken=None, expiration=None, user=None, publicUserInfo=None,):
    self.currentTime = currentTime
    self.authenticationToken = authenticationToken
    self.expiration = expiration
    self.user = user
    self.publicUserInfo = publicUserInfo

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.currentTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.authenticationToken = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.expiration = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.user = evernote.edam.type.ttypes.User()
          self.user.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.publicUserInfo = PublicUserInfo()
          self.publicUserInfo.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AuthenticationResult')
    if self.currentTime != None:
      oprot.writeFieldBegin('currentTime', TType.I64, 1)
      oprot.writeI64(self.currentTime)
      oprot.writeFieldEnd()
    if self.authenticationToken != None:
      oprot.writeFieldBegin('authenticationToken', TType.STRING, 2)
      oprot.writeString(self.authenticationToken)
      oprot.writeFieldEnd()
    if self.expiration != None:
      oprot.writeFieldBegin('expiration', TType.I64, 3)
      oprot.writeI64(self.expiration)
      oprot.writeFieldEnd()
    if self.user != None:
      oprot.writeFieldBegin('user', TType.STRUCT, 4)
      self.user.write(oprot)
      oprot.writeFieldEnd()
    if self.publicUserInfo != None:
      oprot.writeFieldBegin('publicUserInfo', TType.STRUCT, 5)
      self.publicUserInfo.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

