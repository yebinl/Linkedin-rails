class CreateCompanies < ActiveRecord::Migration[5.1]
  def change
    create_table :companies do |t|
      t.string :company_id
      t.string :company_name
      t.string :company_location
      t.string :linkedin_url
      t.string :company_url
      t.string :industry

      t.timestamps
    end
  end
end
