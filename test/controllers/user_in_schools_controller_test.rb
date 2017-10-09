require 'test_helper'

class UserInSchoolsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @user_in_school = user_in_schools(:one)
  end

  test "should get index" do
    get user_in_schools_url
    assert_response :success
  end

  test "should get new" do
    get new_user_in_school_url
    assert_response :success
  end

  test "should create user_in_school" do
    assert_difference('UserInSchool.count') do
      post user_in_schools_url, params: { user_in_school: { degree: @user_in_school.degree, description: @user_in_school.description, end_date: @user_in_school.end_date, fields: @user_in_school.fields, linkedin_id: @user_in_school.linkedin_id, school_id: @user_in_school.school_id, start_date: @user_in_school.start_date, string: @user_in_school.string, user_id: @user_in_school.user_id } }
    end

    assert_redirected_to user_in_school_url(UserInSchool.last)
  end

  test "should show user_in_school" do
    get user_in_school_url(@user_in_school)
    assert_response :success
  end

  test "should get edit" do
    get edit_user_in_school_url(@user_in_school)
    assert_response :success
  end

  test "should update user_in_school" do
    patch user_in_school_url(@user_in_school), params: { user_in_school: { degree: @user_in_school.degree, description: @user_in_school.description, end_date: @user_in_school.end_date, fields: @user_in_school.fields, linkedin_id: @user_in_school.linkedin_id, school_id: @user_in_school.school_id, start_date: @user_in_school.start_date, string: @user_in_school.string, user_id: @user_in_school.user_id } }
    assert_redirected_to user_in_school_url(@user_in_school)
  end

  test "should destroy user_in_school" do
    assert_difference('UserInSchool.count', -1) do
      delete user_in_school_url(@user_in_school)
    end

    assert_redirected_to user_in_schools_url
  end
end
