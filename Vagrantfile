# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network "forwarded_port", guest: 8069, host: 8074, auto_correct: true
  config.vm.network "forwarded_port", guest: 5432, host: 5432, auto_correct: true
  config.vm.synced_folder "src/my_addons", "/home/vagrant/my_addons", create: true
  config.vm.synced_folder "src/addons_enterprise", "/home/vagrant/addons_enterprise", create: true
  config.vm.synced_folder "addons", "/home/vagrant/addons", create: true
  config.vm.synced_folder "addons_bloopark", "/home/vagrant/addons_bloopark", create: true
  config.vm.synced_folder "addons_enterprise", "/home/vagrant/addons_enterprise", create: true
  config.vm.provider "virtualbox" do |vb|
    vb.name = "odoo11"
    vb.cpus = 2
    vb.memory = "2048"
  end
  config.vm.provision "shell", path: "provision/install.sh", privileged: true
end