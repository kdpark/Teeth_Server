.. _ref-friend:

================================
Friend
================================

친구 관계에 해당하는 모듈

Add_Friend 친구추가
-----------------------

친구 추가 API

URL: /add_friend/

Method: POST

.. note:: *현재는 임시로 바로 추가 가능하도록 구현함*

.. warning:: 요청 즉시 친구가 맺어짐

.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - email
     - user의 이메
   * - password
     - 비밀번호 (암호화된 비밀번호)
   * - target
     - 상대방의 이메일



.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 인증실패, 3 input값 없음
   * - Log
     - 설명


