require 'test_helper'

class UserInCompaniesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @user_in_company = user_in_companies(:one)
  end

  test "should get index" do
    get user_in_companies_url
    assert_response :success
  end

  test "should get new" do
    get new_user_in_company_url
    assert_response :success
  end

  test "should create user_in_company" do
    assert_difference('UserInCompany.count') do
      post user_in_companies_url, params: { user_in_company: { company_id: @user_in_company.company_id, description: @user_in_company.description, end_date: @user_in_company.end_date, position: @user_in_company.position, start_date: @user_in_company.start_date, user_id: @user_in_company.user_id } }
    end

    assert_redirected_to user_in_company_url(UserInCompany.last)
  end

  test "should show user_in_company" do
    get user_in_company_url(@user_in_company)
    assert_response :success
  end

  test "should get edit" do
    get edit_user_in_company_url(@user_in_company)
    assert_response :success
  end

  test "should update user_in_company" do
    patch user_in_company_url(@user_in_company), params: { user_in_company: { company_id: @user_in_company.company_id, description: @user_in_company.description, end_date: @user_in_company.end_date, position: @user_in_company.position, start_date: @user_in_company.start_date, user_id: @user_in_company.user_id } }
    assert_redirected_to user_in_company_url(@user_in_company)
  end

  test "should destroy user_in_company" do
    assert_difference('UserInCompany.count', -1) do
      delete user_in_company_url(@user_in_company)
    end

    assert_redirected_to user_in_companies_url
  end
end
