class UserInCompaniesController < ApplicationController
  before_action :set_user_in_company, only: [:show, :edit, :update, :destroy]

  # GET /user_in_companies
  # GET /user_in_companies.json
  def index
    @user_in_companies = UserInCompany.all
  end

  # GET /user_in_companies/1
  # GET /user_in_companies/1.json
  def show
  end

  # GET /user_in_companies/new
  def new
    @user_in_company = UserInCompany.new
  end

  # GET /user_in_companies/1/edit
  def edit
  end

  # POST /user_in_companies
  # POST /user_in_companies.json
  def create
    @user_in_company = UserInCompany.new(user_in_company_params)

    respond_to do |format|
      if @user_in_company.save
        format.html { redirect_to @user_in_company, notice: 'User in company was successfully created.' }
        format.json { render :show, status: :created, location: @user_in_company }
      else
        format.html { render :new }
        format.json { render json: @user_in_company.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /user_in_companies/1
  # PATCH/PUT /user_in_companies/1.json
  def update
    respond_to do |format|
      if @user_in_company.update(user_in_company_params)
        format.html { redirect_to @user_in_company, notice: 'User in company was successfully updated.' }
        format.json { render :show, status: :ok, location: @user_in_company }
      else
        format.html { render :edit }
        format.json { render json: @user_in_company.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /user_in_companies/1
  # DELETE /user_in_companies/1.json
  def destroy
    @user_in_company.destroy
    respond_to do |format|
      format.html { redirect_to user_in_companies_url, notice: 'User in company was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user_in_company
      @user_in_company = UserInCompany.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_in_company_params
      params.require(:user_in_company).permit(:user_id, :company_id, :start_date, :end_date, :position, :description)
    end
end
