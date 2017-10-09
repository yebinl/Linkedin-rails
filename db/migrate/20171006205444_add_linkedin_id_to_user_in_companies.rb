class AddLinkedinIdToUserInCompanies < ActiveRecord::Migration[5.1]
  def change
    add_column :user_in_companies, :linkedin_id, :string
  end
end
