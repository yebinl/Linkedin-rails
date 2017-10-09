class AddActiveToUserInCompanies < ActiveRecord::Migration[5.1]
  def change
    add_column :user_in_companies, :active, :string
  end
end
