class UserInSchoolsController < ApplicationController
  before_action :set_user_in_school, only: [:show, :edit, :update, :destroy]

  # GET /user_in_schools
  # GET /user_in_schools.json
  def index
    @user_in_schools = UserInSchool.all
  end

  # GET /user_in_schools/1
  # GET /user_in_schools/1.json
  def show
  end

  # GET /user_in_schools/new
  def new
    @user_in_school = UserInSchool.new
  end

  # GET /user_in_schools/1/edit
  def edit
  end

  # POST /user_in_schools
  # POST /user_in_schools.json
  def create
    @user_in_school = UserInSchool.new(user_in_school_params)

    respond_to do |format|
      if @user_in_school.save
        format.html { redirect_to @user_in_school, notice: 'User in school was successfully created.' }
        format.json { render :show, status: :created, location: @user_in_school }
      else
        format.html { render :new }
        format.json { render json: @user_in_school.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /user_in_schools/1
  # PATCH/PUT /user_in_schools/1.json
  def update
    respond_to do |format|
      if @user_in_school.update(user_in_school_params)
        format.html { redirect_to @user_in_school, notice: 'User in school was successfully updated.' }
        format.json { render :show, status: :ok, location: @user_in_school }
      else
        format.html { render :edit }
        format.json { render json: @user_in_school.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /user_in_schools/1
  # DELETE /user_in_schools/1.json
  def destroy
    @user_in_school.destroy
    respond_to do |format|
      format.html { redirect_to user_in_schools_url, notice: 'User in school was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user_in_school
      @user_in_school = UserInSchool.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_in_school_params
      params.require(:user_in_school).permit(:user_id, :school_id, :start_date, :end_date, :degree, :description, :fields, :linkedin_id, :string)
    end
end
