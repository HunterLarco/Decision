//
//  VotingViewController.swift
//  Pods
//
//  Created by Luke Solomon on 12/11/15.
//
//

import UIKit
import Alamofire

class VotingViewController:UIViewController {
    
    @IBOutlet weak var MainView: UIView!
    
    @IBOutlet weak var voteNoView: UIView!
    @IBOutlet weak var voteYesView: UIView!
    
    @IBOutlet weak var voteNoButton: UIButton!
    @IBOutlet weak var voteYesButton: UIButton!
    
    
    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        
        UIView.animateWithDuration(0.5, delay: 0.0, options: UIViewAnimationOptions.CurveEaseOut, animations: {

            self.view.layoutIfNeeded()
            }, completion: nil)
        
    }
    
    
    @IBAction func yesButtonTapped(sender: AnyObject) {
        
        UIView.animateWithDuration(0.3, delay:0.0, options:UIViewAnimationOptions.CurveEaseOut ,animations: {
            self.voteNoView.alpha = 0
            self.voteYesView.alpha = 0
            self.voteNoButton.userInteractionEnabled = false
            self.voteYesButton.userInteractionEnabled = false
            }, completion: {(_) -> Void in
        })
//        getRequestToApiWithString("yep")
    }
    
    @IBAction func noButtonTapped(sender: AnyObject) {
        UIView.animateWithDuration(0.3, delay:0.0, options:UIViewAnimationOptions.CurveEaseOut ,animations: {
            self.voteNoView.alpha = 0
            self.voteYesView.alpha = 0
            self.voteNoButton.userInteractionEnabled = false
            self.voteYesButton.userInteractionEnabled = false
            }, completion: {(_) -> Void in
        })
//        getRequestToApiWithString("nope")
    }

    func getRequestToApiWithString(string:NSString) {
        
        Alamofire.request(.POST, "\(BASEURL)" , parameters: nil)
            .responseJSON { response in
                if let JSON = response.result.value {
                    
                    
                    dispatch_async(dispatch_get_main_queue(), {
                        
                    })
                }
        }
    }

    
}