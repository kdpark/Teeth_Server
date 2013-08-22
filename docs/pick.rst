.. _ref-pick:

================================
Pick
================================

주선자와 소개팅 대상에 관련된 모듈


Main (main화면)
-----------------------

main 화면에 필요한 정보를 리턴한다.

URL: /main/

Method: POST


.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소



.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 유저, 3 친구 모자람, 4 오늘의 chance 모두 소모
   * - Log
     - 메세지
   * - Value
     - 3 오류 시, 현재 친구 수를 리턴한다. 현재 3명미만은 오류를 유발시키게 구현되어있다.
   * - arranger_now
     - 주선자 이름
   * - arranger_now_pic
     - 주선자 프로필 사진
   * - candidate_now
     - 후보자 이름
   * - candidate_now_pic
     - 후보자 프로필 사진
   * - candidate_num
     - 대기자 수


Pick candidate (후보자 선택)
-----------------------------

상대방을 선택하는 API, 해당 사용자의 chance 를 OFF(2) 로 만들고 후보자의 전화번호를 리턴받아온다.

URL : /pick_candidate/


.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 사용자
   * - candidate_phone
     - 후보자의 전화번호
   * - candidate_pic
     - 후보자 사진


소개팅 요청 목록 보기
-----------------------------

상대방에게 요청한 소개팅이나, 사용자가 받은 모든 요청 목록을 리턴한다.

URL : /view_meeting_req/


.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 사용자
   * - send_list
     - 내가 보낸 소개팅 리스트 ('name': 상대방이름, 'user_id': user id, 'profile_pic': 프사 주소)
   * - send_num
     - 내가 보낸 소개팅 수
   * - receive_list
     - 내가 받은 소개팅 리스트 ('name': 상대방이름, 'user_id': user id, 'profile_pic': 프사 주소)
   * - receive_num
     - 내가 받은 소개팅 수

New Cycle (새로운 상대방 찾기)
--------------------------------------

이 API를 날리면, 모든 사용자에게 새로운 상대방을 매칭시켜준다.
오후 10시 등, 정해진 시간에 날리면 됨.
어드민 id와 비번이 필요하다.

URL : /new_cycle/

.. warning:: API 성공 시, 기존에 있던 상대방 후보자는 새로운 후보자로 대체된다.

.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - adminid
     - 트렐로 참고 (admin과 같음)
   * - password
     - 트렐로 참고할 것. (admin)


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 사용자

