class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :first_name
      t.string :last_name
      t.string :linkedin_id
      t.string :linkedin_url
      t.string :description

      t.timestamps
    end
  end
end
