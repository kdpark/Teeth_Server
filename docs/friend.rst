.. _ref-friend:

================================
Friend
================================

친구 관계에 해당하는 모듈

Add_Friend 친구추가
-----------------------

소개슈머 자체 가입한 사람은 email로,
facebook으로 가입한 사람은 페북key를 사용해서 강제로 친구를 맺게한다.
beta 때 까지만 한시적으로 운영하는 함수


URL: /add_friend/

Method: POST

.. note:: *현재는 임시로 바로 추가 가능하도록 구현함*

.. warning:: 요청 즉시 친구가 맺어짐

.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소
   * - target
     - 상대방의 이메일 또는 페북key값.



.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 인증실패, 3 input값 없음
   * - Log
     - 설명


Sync friend 친구추가
-----------------------

전화번호 목록과 페북 친구 목록을 전송해주면,
현재 가입자목록과 비교하여 친구를 자동으로 맺게해줌.

URL: /sync_friend/

Method: POST

.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소
   * - fb_friend
     - 페북친구들의 key 목록 (csv 형식)
   * - phone_contact
     - 전화번호 목록 (csv 형식, 회원가입 양식 참조)


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 인증실패
   * - Log
     - 설명


