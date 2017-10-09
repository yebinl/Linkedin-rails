class CreateUserInCompanies < ActiveRecord::Migration[5.1]
  def change
    create_table :user_in_companies do |t|
      t.string :user_id
      t.string :company_id
      t.string :start_date
      t.string :end_date
      t.string :position
      t.string :description

      t.timestamps
    end
  end
end
